using System;
using System.Collections.Generic;
using System.Diagnostics;

public class FindMergeSolution
{
    /// <summary>
    /// A simple Node class.
    /// </summary>
    /// <typeparam name="T">The type of Data.</typeparam>
    public class Node<T>
    {
        public T Data { get; set; }
        public Node<T> Next { get; set; }

        public Node(T data, Node<T> next = null)
        {
            Data = data;
            Next = next;
        }
    }

    /// <summary>
    /// Given the heads of two linked lists, returns the node where they merge
    /// (or null if they don't merge).
    /// </summary>
    /// <typeparam name="T">The type of Data,</typeparam>
    /// <param name="head1">The head of the first linked list.</param>
    /// <param name="head2">The head of the second linked list.</param>
    /// <returns>The Node where they merge, or null.</returns>
    public static Node<T> FindMerge<T>(Node<T> head1, Node<T> head2)
    {
        // Find the length of each linked list.
        var len1 = 0;
        for (var p = head1; p != null; p = p.Next)
        {
            len1++;
        }
        var len2 = 0;
        for (var p = head2; p != null; p = p.Next)
        {
            len2++;
        }

        // Adjust the heads so that they are equidistant from the end.
        for (; len1 > len2; len1--)
        {
            head1 = head1.Next;
        }
        for (; len2 > len1; len2--)
        {
            head2 = head2.Next;
        }

        // Compare one-by-one until a match is found.
        while (head1 != null)
        {
            if (head1 == head2)
            {
                return head1;
            }
            head1 = head1.Next;
            head2 = head2.Next;
        }
        return null;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var a5 = new Node<int>(5);
        var a4 = new Node<int>(4, a5);
        var a3 = new Node<int>(3, a4);
        var a2 = new Node<int>(2, a3);
        var a1 = new Node<int>(1, a2);
        var b1 = new Node<int>(1, a3);
        var b0 = new Node<int>(0, b1);
        var c5 = new Node<int>(5);
        var c4 = new Node<int>(4, c5);
        var c3 = new Node<int>(3, c4);
        var c2 = new Node<int>(2, c3);
        var testHead1s = new[] { a1, b1, c2 };
        var testHead2s = new[] { a2, a2, a2 };
        Debug.Assert(testHead1s.Length == testHead2s.Length);
        for (var i = 0; i < testHead1s.Length; i++)
        {
            Console.WriteLine("Test Case #{0}:", i + 1);
            var mergeNode = FindMerge<int>(testHead1s[i], testHead2s[2]);
            string message = null;
            if (mergeNode != null)
            {
                message = string.Format("Merged at: {0}.", mergeNode.Data);
            }
            else
            {
                message = "No merge node detected.";
            }
            Console.WriteLine("    " + message);
        }
    }
}